import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SeasonalStrength': 1.0
        })
    )
