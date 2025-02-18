import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ModifiedRSI': 1.0
        })
    )
