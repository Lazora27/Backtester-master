import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und GannAngles
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'GannAngles': 1.0
        })
    )
