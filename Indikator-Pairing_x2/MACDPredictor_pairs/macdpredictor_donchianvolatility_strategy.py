import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DonchianVolatility': 1.0
        })
    )
