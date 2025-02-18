import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
