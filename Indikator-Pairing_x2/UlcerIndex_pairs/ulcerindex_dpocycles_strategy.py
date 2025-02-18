import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
