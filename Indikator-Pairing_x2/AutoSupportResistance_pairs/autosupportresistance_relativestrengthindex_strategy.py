import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
