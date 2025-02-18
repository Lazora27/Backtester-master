import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DeltaProfile': 1.0
        })
    )
