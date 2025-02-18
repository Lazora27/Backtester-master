import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SmoothedRSI': 1.0
        })
    )
