import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'GannFans': 1.0
        })
    )
