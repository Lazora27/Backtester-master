import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'GannFans': 1.0
        })
    )
