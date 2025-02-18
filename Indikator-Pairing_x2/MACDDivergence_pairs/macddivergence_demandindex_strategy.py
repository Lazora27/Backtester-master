import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DemandIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DemandIndex': 1.0
        })
    )
