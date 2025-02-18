import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
