import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'DemandIndex': 1.0
        })
    )
