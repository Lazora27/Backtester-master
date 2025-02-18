import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'TrendCycles': 1.0
        })
    )
