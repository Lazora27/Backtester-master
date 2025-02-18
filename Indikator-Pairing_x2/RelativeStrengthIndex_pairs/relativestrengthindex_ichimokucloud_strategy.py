import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
