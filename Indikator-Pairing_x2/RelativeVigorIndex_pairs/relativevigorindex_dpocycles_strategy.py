import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
