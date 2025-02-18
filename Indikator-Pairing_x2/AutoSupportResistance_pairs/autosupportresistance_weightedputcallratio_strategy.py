import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
