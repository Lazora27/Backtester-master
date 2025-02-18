import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PutCallRatio': 1.0
        })
    )
