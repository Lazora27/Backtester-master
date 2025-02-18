import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
