import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und FisherTransform
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'FisherTransform': 1.0
        })
    )
