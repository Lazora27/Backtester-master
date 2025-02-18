import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'GannFans': 1.0
        })
    )
