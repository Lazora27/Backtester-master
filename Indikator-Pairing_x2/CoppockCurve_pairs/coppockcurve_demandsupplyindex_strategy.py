import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
