import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'DPOCycles': 1.0
        })
    )
