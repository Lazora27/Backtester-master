import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
