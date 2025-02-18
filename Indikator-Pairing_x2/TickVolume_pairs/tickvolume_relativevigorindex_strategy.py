import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
