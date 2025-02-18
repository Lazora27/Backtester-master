import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
