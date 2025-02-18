import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
