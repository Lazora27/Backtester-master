import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
