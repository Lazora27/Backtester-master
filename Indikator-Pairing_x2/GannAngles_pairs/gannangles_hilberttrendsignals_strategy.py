import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
