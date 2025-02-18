import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und CyberCycle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'CyberCycle': 1.0
        })
    )
