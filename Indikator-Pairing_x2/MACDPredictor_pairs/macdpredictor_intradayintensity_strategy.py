import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'IntradayIntensity': 1.0
        })
    )
