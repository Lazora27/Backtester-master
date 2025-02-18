import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'LiquidityIndex': 1.0
        })
    )
