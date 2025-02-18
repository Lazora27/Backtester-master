import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
