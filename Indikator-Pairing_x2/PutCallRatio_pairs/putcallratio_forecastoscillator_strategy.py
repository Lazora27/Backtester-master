import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ForecastOscillator': 1.0
        })
    )
