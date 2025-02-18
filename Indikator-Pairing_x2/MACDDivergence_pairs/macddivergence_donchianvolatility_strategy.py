import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DonchianVolatility': 1.0
        })
    )
