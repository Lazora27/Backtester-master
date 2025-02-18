import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'HilbertTrendline': 1.0
        })
    )
