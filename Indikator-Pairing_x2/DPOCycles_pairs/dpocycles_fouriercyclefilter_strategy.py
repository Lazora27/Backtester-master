import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
