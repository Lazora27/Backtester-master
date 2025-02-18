import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
