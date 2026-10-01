export const wrapDelta = degrees => ((degrees + 540) % 360 + 360) % 360 - 180;
export const snapTurn = (turn, count) => Math.round(turn / (360 / count)) * (360 / count);
export const indexAt = (turn, count) => ((Math.round(-turn / (360 / count)) % count) + count) % count;
export function coastStep(velocity, ms) {
  const decay = Math.exp(-ms / 340);
  return { distance: velocity * 340 * (1 - decay), velocity: velocity * decay };
}
