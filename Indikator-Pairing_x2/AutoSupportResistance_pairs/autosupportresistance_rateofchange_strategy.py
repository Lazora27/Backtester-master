import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und RateOfChange
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'RateOfChange': 1.0
        })
    )
