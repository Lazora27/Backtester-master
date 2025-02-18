import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SeasonalStrength': 1.0
        })
    )
