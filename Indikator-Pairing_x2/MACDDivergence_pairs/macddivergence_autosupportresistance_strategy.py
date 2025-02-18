import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AutoSupportResistance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AutoSupportResistance
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AutoSupportResistance': 1.0
        })
    )
