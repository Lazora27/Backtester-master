import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'DPOCycles': 1.0
        })
    )
