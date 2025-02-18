import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
