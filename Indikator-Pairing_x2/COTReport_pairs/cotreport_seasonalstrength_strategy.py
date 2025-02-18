import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SeasonalStrength': 1.0
        })
    )
