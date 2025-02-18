import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
