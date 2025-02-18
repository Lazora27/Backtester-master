import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
