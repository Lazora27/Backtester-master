import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
