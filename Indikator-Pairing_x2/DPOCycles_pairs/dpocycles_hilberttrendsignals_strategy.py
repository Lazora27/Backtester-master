import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
