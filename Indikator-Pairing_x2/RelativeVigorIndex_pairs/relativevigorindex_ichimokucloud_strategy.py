import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
