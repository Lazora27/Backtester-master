import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
